from ptcgo.game.card_effects.pokemon import is_energy_card, is_psychic_energy
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def recover(ctx):
    """One Psychic Energy off Mewtwo for six damage counters off itself."""
    discarded = await ctx.discard_energy_from(ctx.attacker, 1,
                                              predicate=is_psychic_energy)
    if discarded and ctx.attacker is not None:
        await ctx.heal(60, ctx.attacker)

card = PokemonCardDef(
    guid="56a8af55-0d7d-59c9-af4e-de73f453caf7",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo",
    searchable_by=["Mewtwo", "Basic", "Mewtwo"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="DP5",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Energy Absorption",
            game_text="Search your discard pile for up to 2 Energy cards and attach them to Mewtwo.",
            cost={},
            effect=attach_from_discard(is_energy_card, count=2,
                                      target="self"),
        ),
        Attack(
            title="Recover",
            game_text="Discard a Psychic Energy attached to Mewtwo and remove 6 damage counters from Mewtwo.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=recover,
        ),
        Attack(
            title="Psyburn",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)