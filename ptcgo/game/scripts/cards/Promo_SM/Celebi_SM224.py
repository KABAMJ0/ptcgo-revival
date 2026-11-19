from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

async def call_for_greatness(ctx):
    """Search the deck for up to 3 Pokemon-GX with different names."""
    from ptcgo.game.card_effects.pokemon import is_pokemon_gx
    from ptcgo.game.data_utils import def_for
    named = []
    for _ in range(3):
        def candidate(card):
            if not is_pokemon_gx(card.archetype_id):
                return False
            name = getattr(def_for(card.archetype_id), "display_name", "")
            return name not in named
        picks = await ctx.search_deck(candidate, count=1, minimum=0,
                                      prompt="Choose a Pokemon-GX")
        if not picks:
            break
        card = picks[0]
        named.append(getattr(def_for(card.archetype_id), "display_name", ""))
        await ctx.put_in_hand([card], reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="49e117c1-7dcc-56ab-8492-4adf1b30eadb",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name",
    display_name="Celebi",
    searchable_by=["Celebi", "Basic", "Celebi"],
    subtypes=["Basic"],
    collector_number=224,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=251,
    abilities=[
        Attack(
            title="Call for Greatness",
            game_text="Search your deck for up to 3 Pok\u00e9mon-GX with different names, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=call_for_greatness,
        ),
        Attack(
            title="Psy Bolt",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)