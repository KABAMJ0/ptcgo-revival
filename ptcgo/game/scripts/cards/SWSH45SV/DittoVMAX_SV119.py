from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

async def nine_tailed_shapeshifter(ctx):
    """Choose 1 of the opponent's Active Pokemon's attacks and use it."""
    defender = ctx.defender
    if defender is None:
        return
    definition = def_for(defender.archetype_id)
    attacks = [a for a in getattr(definition, "abilities", []) if isinstance(a, Attack)]
    if not attacks:
        return
    candidates = [(defender, atk) for atk in attacks]
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    await ctx.use_attack(chosen)

card = PokemonCardDef(
    guid="36cf5825-57e9-5d09-bef5-ea64271aa899",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DittoVMAX.Name",
    display_name="Ditto VMAX",
    searchable_by=["Ditto VMAX", "VMAX", "DittoVMAX"],
    subtypes=["VMAX"],
    collector_number=119,
    set_code="SWSH45SV",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DittoV.Name",
    family_id=132,
    abilities=[
        Attack(
            title="Max Transform",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=nine_tailed_shapeshifter,
        ),
    ],
)