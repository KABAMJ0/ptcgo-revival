from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

async def _energy_salon(ctx):
    """Search the deck for 3 basic Energy of different types."""
    chosen = []
    types_taken = set()
    for _ in range(3):
        def _pick(card):
            if not is_basic_energy_card(card):
                return False
            types = set(card.get_attribute(AttrID.POKEMON_TYPES) or [])
            return not (types & types_taken)
        picks = await ctx.search_deck(_pick, count=1, minimum=0,
                                      prompt="Choose a basic Energy of a new type")
        if not picks:
            break
        card = picks[0]
        types_taken |= set(card.get_attribute(AttrID.POKEMON_TYPES) or [])
        chosen.append(card)
    if chosen:
        await ctx.put_in_hand(chosen, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="29471471-558b-59b3-a8f0-ddca55de7496",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1", "Delcatty"],
    subtypes=["Stage 1"],
    collector_number=105,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Attack(
            title="Energy Salon",
            game_text="Search your deck for 3 different types of basic Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_energy_salon,
        ),
        Attack(
            title="Fake Out",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)