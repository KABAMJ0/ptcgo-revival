from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2f310d96-7827-540b-aa04-fba46495cd0d",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=39,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=230,
    abilities=[
        Attack(
            title="Gather Strength",
            game_text="Search your deck for up to 4 basic Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(predicate=is_basic_energy_card, count=4, minimum=0),
        ),
        Attack(
            title="Dragon Blast",
            game_text="Discard a Water and a Lightning Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.LIGHTNING: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)