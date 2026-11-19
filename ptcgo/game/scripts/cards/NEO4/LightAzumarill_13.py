from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

from ptcgo.game.card_effects.support_common import distribute_energy, remove_self_from_play


async def bubble_jump(ctx):
    """Printed 30 (dealt by remove_self_from_play below); on heads 2 Energy
    move to a Benched Pokemon and Light Azumarill returns to your hand."""
    bench = ctx.my_bench()
    if not bench:
        return
    heads = await ctx.flip_coins(1, "Bubble Jump")
    if not (heads and heads[0]):
        return
    energies = list(ctx.attached_energies(ctx.attacker))[:2]
    if energies:
        picks = await ctx.choose_cards(
            energies, 2, minimum=0, prompt="Choose up to 2 Energy to move")
        if picks:
            await distribute_energy(ctx, list(picks), bench)
    await remove_self_from_play(destination="hand", with_attachments="same")(ctx)

card = PokemonCardDef(
    guid="5ea3b1df-08ca-5e1c-a6e8-5cd2d5f655a0",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightAzumarill.Name",
    display_name="Light Azumarill",
    searchable_by=["Light Azumarill", "Stage 1", "LightAzumarill"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=184,
    abilities=[
        Attack(
            title="Bubble",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Bubble Jump",
            game_text="If you have any Benched Pok\u00e9mon, flip a coin. If heads, take 2 Energy cards attached to Light Azumarill and attach them to 1 of your Benched Pok\u00e9mon. Then return Light Azumarill and all cards attached to it to your hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=bubble_jump,
        ),
    ],
)