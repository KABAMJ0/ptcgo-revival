from ptcgo.game.card_effects.pokemon import is_pokemon_card
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7b95c05f-c148-56a7-9497-e32e09704e1a",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=79,
    abilities=[
        Attack(
            title="Fishing Tail",
            game_text="Search your discard pile for a Baby Pok\u00e9mon, Basic Pok\u00e9mon, Evolution card, or basic Energy card, show it to your opponent, and then put it into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(lambda card: is_pokemon_card(card) or is_basic_energy_card(card),
                                 count=1, reveal=True, to="hand",
                                 prompt="Choose a card from your discard pile"),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)