from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import search_attach_energy


def _lightning(card):
    return energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def attract_current(ctx):
    """Printed 20, then one Lightning Energy per heads searched onto one of your
    Lightning Pokemon."""
    await ctx.deal_damage()
    flips = await ctx.flip_coins(3, "Attract Current")
    heads = sum(1 for flip in flips if flip)
    targets = [p for p in ctx.my_pokemon_in_play()
               if PokemonTypes.LIGHTNING.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])]
    for _ in range(heads):
        if not targets:
            break
        picks = await ctx.search_deck(_lightning, count=1, minimum=0,
                                      prompt="Choose a Lightning Energy to attach")
        if not picks:
            break
        holder = await ctx.choose_pokemon(targets, "Choose a Lightning Pokemon to attach it to")
        if holder is None:
            break
        await ctx.attach_energy(picks[0], holder)
    if heads:
        await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="635602fb-00ef-5970-8590-85655bb373ee",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=["Ampharos", "Stage 2", "Ampharos"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=180,
    abilities=[
        Attack(
            title="Attract Current",
            game_text="Flip 3 coins. For each heads, you may search your deck for a Lightning Energy card and attach it to 1 of your Lightning Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=attract_current,
        ),
        Attack(
            title="Gigavolt",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 20 more damage. If tails, this attack does 40 damage and the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)