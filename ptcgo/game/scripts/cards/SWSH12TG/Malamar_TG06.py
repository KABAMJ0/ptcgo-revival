from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for

async def rapid_strike_tentacles(ctx):
    """Reveal any number of Rapid Strike cards from your hand. This attack
    does 40 damage for each card revealed in this way. Then, shuffle those
    cards into your deck."""
    candidates = [c for c in ctx.hand() if "Rapid Strike" in subtypes_for(c.archetype_id)]
    picks = []
    if candidates:
        picks = await ctx.choose_cards(
            candidates, len(candidates), minimum=0,
            prompt="Reveal any number of Rapid Strike cards from your hand.",
        )
    if picks:
        await ctx.reveal_cards(picks)
    await ctx.deal_damage(40 * len(picks))
    if picks:
        await ctx.shuffle_into_deck(picks)

card = PokemonCardDef(
    guid="9aab4b80-9169-52e0-8dbf-f7526802380b",
    key="SWSH12TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=["Malamar", "Stage 1", "Rapid Strike", "Malamar"],
    subtypes=["Stage 1", "Rapid Strike"],
    collector_number=6,
    set_code="SWSH12TG",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=687,
    abilities=[
        Attack(
            title="Rapid Strike Tentacles",
            game_text="Reveal any number of Rapid Strike cards from your hand. This attack does 40 damage for each card you revealed in this way. Then, shuffle those cards into your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            damage_operator="x",
            effect=rapid_strike_tentacles,
        ),
    ],
)