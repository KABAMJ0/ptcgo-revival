from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID

async def super_fang(ctx):
    """Damage counters on the opponent's Active until its remaining HP is 10."""
    target = ctx.defender
    if target is None:
        return
    hp = target.get_attribute(AttrID.HP, 0)
    if hp > 10:
        await ctx.deal_damage(hp - 10, target=target, as_counters=True)

card = PokemonCardDef(
    guid="08daf3c0-d0e2-50f5-abf5-c7699ec7caa9",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medichamex.Name",
    display_name="Medicham ex",
    searchable_by=["Medicham ex", "Stage 1", "ex", "Medichamex"],
    subtypes=["Stage 1", "ex"],
    collector_number=161,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title="Chi-Atsu",
            game_text="Put damage counters on your opponent's Active Pok\u00e9mon until its remaining HP is 50.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=super_fang,
        ),
        Attack(
            title="Yoga Kick",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=190,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)