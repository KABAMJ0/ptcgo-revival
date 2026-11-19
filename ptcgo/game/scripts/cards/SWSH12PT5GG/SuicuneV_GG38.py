from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import in_active_spot
from ptcgo.game.card_effects.attacks_common import damage_per, count_bench


async def _fleet_footed(ctx):
    if await ctx.ask_yes_no("Draw a card?"):
        await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="cb177572-6fc7-52ea-9434-0a6ffbd58e85",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SuicuneV.Name",
    display_name="Suicune V",
    searchable_by=["Suicune V", "Basic", "V", "SuicuneV"],
    subtypes=["Basic", "V"],
    collector_number=38,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Ability(
            title="Fleet-Footed",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may draw a card.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=_fleet_footed,
        ),
        Attack(
            title="Blizzard Rondo",
            game_text="This attack does 20 more damage for each Benched Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_bench("both"), 20, base=20),
        ),
    ],
)