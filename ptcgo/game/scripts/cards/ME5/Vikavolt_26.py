from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import named
from ptcgo.game.card_effects.attacks_common import snipe_attack


async def giga_railgun(ctx):
    """Printed damage only while a Voltaic Lightning Energy is attached."""
    has_voltaic = any(
        named("Voltaic Lightning Energy")(energy)
        for energy in ctx.attached_energies(ctx.attacker))
    if has_voltaic:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="eed6092d-261f-59a5-8818-746df72cd225",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vikavolt.Name",
    display_name="Vikavolt",
    searchable_by=["Vikavolt", "Stage 2", "Vikavolt"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    family_id=736,
    abilities=[
        Attack(
            title="Quick Dive",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=snipe_attack(50, pool="any", count=1, apply_modifiers=False),
        ),
        Attack(
            title="Giga Railgun",
            game_text="If this Pok\u00e9mon has no Voltaic Lightning Energy attached, this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=260,
            effect=giga_railgun,
        ),
    ],
)