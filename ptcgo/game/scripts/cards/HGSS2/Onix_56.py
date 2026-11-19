from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _energy_healer(ctx):
    if ctx.attaching_player_id == ctx.player_id:
        await ctx.heal(10, ctx.source)


card = PokemonCardDef(
    guid="cddd0f8d-49c1-57d2-b46c-8e5172fb6de3",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    display_name="Onix",
    searchable_by=["Onix", "Basic", "Onix"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="HGSS2",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=95,
    abilities=[
        Ability(
            title="Energy Healer",
            game_text="Whenever you attach an Energy card from your hand to Onix, remove a damage counter from Onix.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_energy_healer,
        ),
        Attack(
            title="Boundless Power",
            game_text="Onix can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=unimplemented,
        ),
    ],
)