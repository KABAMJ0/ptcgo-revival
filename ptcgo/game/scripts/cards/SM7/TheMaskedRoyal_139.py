from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities, AttrID, PokemonStage, PokemonTypes
from ptcgo.game.card_effects.trainers import is_basic_energy_card


async def the_masked_royal(ctx):
    """Attach 1 basic Energy card from your hand to 1 of your Stage 2 Grass,
    Fire, or Water Pokemon."""
    wanted = {PokemonTypes.GRASS.value, PokemonTypes.FIRE.value, PokemonTypes.WATER.value}
    energies = [c for c in ctx.hand() if is_basic_energy_card(c)]
    targets = [p for p in ctx.my_pokemon_in_play()
               if p.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value
               and wanted & set(p.get_attribute(AttrID.POKEMON_TYPES) or [])]
    if not energies or not targets:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a basic Energy card to attach")
    if not picks:
        return
    target = (await ctx.choose_pokemon(targets, "Choose a Stage 2 Pokemon to attach it to")
              if len(targets) > 1 else targets[0])
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)


card = SupporterCardDef(
    guid="82d93bf4-a25f-5210-94ce-bccc27c2168e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TheMaskedRoyal.Name",
    display_name="The Masked Royal",
    searchable_by=["The Masked Royal", "Supporter"],
    subtypes=["Supporter"],
    collector_number=139,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=the_masked_royal
)
