from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from ptcgo.game.session.passives import Passive
from ptcgo.game.session.effects import is_trainer_card


class WeatherReadingPassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        discard = board.find_player_area(carrier.owning_player_id, "discard")
        count = sum(
            1 for c in (discard.children if discard else [])
            if is_trainer_card(c)
            and c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value
        )
        if count >= 8:
            return {}
        return cost


async def _weather_force(ctx):
    await ctx.deal_damage()
    await ctx.draw_until(6)


card = PokemonCardDef(
    guid="79359854-86c3-58a6-b5f5-cf61a0df1db1",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Castform.Name",
    display_name="Castform",
    searchable_by=["Castform", "Basic", "Castform"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="SWSH11TG",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=351,
    abilities=[
        Ability(
            title="Weather Reading",
            game_text="If you have 8 or more Stadium cards in your discard pile, ignore all Energy in this Pok\u00e9mon's attack costs.",
            passive=WeatherReadingPassive(),
        ),
        Attack(
            title="Weather Force",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=_weather_force,
        ),
    ],
)