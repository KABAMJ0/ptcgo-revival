from ptcgo.game.card_effects.pokemon import is_lightning_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.content.definitions import def_for
from ptcgo.game.session.passives import Passive, carrier_pokemon

class SynchronizedLiftPassive(Passive):
    """Retreat Cost is 0 while both partner birds are on the same side."""

    PARTNERS = ('Articuno ex', 'Moltres ex')

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        names = set()
        for ally in board.pokemon_in_play(pokemon.owning_player_id):
            definition = def_for(ally.archetype_id)
            if definition is not None and definition.display_name:
                names.add(definition.display_name)
        return 0 if all(partner in names for partner in self.PARTNERS) else cost



async def thunder_gift(ctx):
    await ctx.deal_damage()
    me = ctx.attacker
    others = [pokemon for pokemon in ctx.my_pokemon_in_play() if pokemon is not me]
    if not others:
        return
    await ctx.move_energy_freely(
        [me], others, predicate=is_lightning_energy, max_count=1,
        prompt="Move a Lightning Energy to another Pokémon",
    )

card = PokemonCardDef(
    guid="84c33a50-efc4-5c0d-8ea7-f7f2356a41d9",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdosex.Name",
    display_name="Zapdos ex",
    searchable_by=["Zapdos ex", "Basic", "EX", "Zapdosex"],
    subtypes=["Basic", "EX"],
    collector_number=33,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=145,
    abilities=[
        Ability(
            title="Synchronized Lift",
            game_text="As long as you have Articuno ex and Moltres ex in play, the Retreat Cost for Zapdos ex is 0.",
            passive=SynchronizedLiftPassive(),
        ),
        Attack(
            title="Thunder Gift",
            game_text="You may move a Lightning Energy card attached to Zapdos ex to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=thunder_gift,
        ),
        Attack(
            title="Lightning Wing",
            game_text="Does 10 damage to 1 of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)