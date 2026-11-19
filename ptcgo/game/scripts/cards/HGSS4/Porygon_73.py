from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _recover(ctx):
    energies = ctx.attached_energies(ctx.attacker)
    if not energies:
        return
    pick = energies if len(energies) == 1 else await ctx.choose_cards(
        energies, 1, prompt="Choose an Energy to discard from Porygon")
    if not pick:
        return
    await ctx.discard_cards([pick[0]])
    await ctx.heal(40, ctx.attacker)

card = PokemonCardDef(
    guid="8ac59b7d-2cdd-56a8-afd8-536223dcfe71",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    display_name="Porygon",
    searchable_by=["Porygon", "Basic", "Porygon"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="HGSS4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=137,
    abilities=[
        Attack(
            title="Sharpen",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Recover",
            game_text="Discard an Energy attached to Porygon and remove 4 damage counters from Porygon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_recover,
        ),
    ],
)