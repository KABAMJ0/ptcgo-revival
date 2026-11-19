from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_bench, damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.card_effects.pokemon import in_active_spot
from ptcgo.game.card_effects.attacks_common import damage_per, count_bench

async def _fleet_footed(ctx):
    if await ctx.ask_yes_no("Draw a card?"):
        await ctx.draw_cards(1)

card = PokemonCardDef(
    guid="6e6bbd53-859e-5c10-b5fa-a03473a109d3",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EnteiV.Name",
    display_name="Entei V",
    searchable_by=["Entei V", "Basic", "V", "EnteiV"],
    subtypes=["Basic", "V"],
    collector_number=36,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloV,
    hp=230,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Ability(
            title="Fleet-Footed",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may draw a card.",
            effect=_fleet_footed,
            condition=in_active_spot,
        ),
        Attack(
            title="Burning Rondo",
            game_text="This attack does 20 more damage for each Benched Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_bench("both"), 20, base=20),
        ),
    ],
)