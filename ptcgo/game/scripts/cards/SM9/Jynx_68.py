from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

async def _mysterious_dance(ctx):
    """1 damage counter per Benched Pokemon on the opponent's side, placed on
    any of their Pokemon as the player likes."""
    count = len(ctx.opponent_bench())
    if count <= 0:
        return
    await ctx.place_damage_counters(count, ctx.opponent_pokemon_in_play())

card = PokemonCardDef(
    guid="744aa9f0-4eb1-5aea-b9d7-41f7abfdfb1b",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic", "Jynx"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=124,
    abilities=[
        Attack(
            title="Dazzle Dance",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Mysterious Dance",
            game_text="For each of your opponent's Benched Pok\u00e9mon, put 1 damage counter on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=_mysterious_dance,
        ),
    ],
)