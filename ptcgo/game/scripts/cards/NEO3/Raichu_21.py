from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

from ptcgo.game.card_effects.pokemon import energy_provides_type


async def lightning_strike(ctx):
    """Printed 40; discarding all Lightning Energy from Raichu makes it 80."""
    lightning = [e for e in ctx.attached_energies(ctx.attacker)
                 if energy_provides_type(e, PokemonTypes.LIGHTNING.value)]
    if not lightning:
        await ctx.deal_damage()
        return
    if not await ctx.ask_yes_no("Discard all Lightning Energy from Raichu for 80 damage?"):
        await ctx.deal_damage()
        return
    await ctx.discard_cards(lightning)
    await ctx.deal_damage(80)

card = PokemonCardDef(
    guid="287ada76-71fb-5fa5-919f-da50e3ca12c4",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1", "Raichu"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=26,
    abilities=[
        Attack(
            title="Thundershock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Lightning Strike",
            game_text="You may discard all Lightning Energy cards attached to Raichu. If you do, this attack does 80 damage.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=40,
            effect=lightning_strike,
        ),
    ],
)