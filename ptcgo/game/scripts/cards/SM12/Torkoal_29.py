from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type, is_energy_card
from ptcgo.game.card_effects.support_common import recover_from_discard


def _is_fire_energy(card) -> bool:
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)

card = PokemonCardDef(
    guid="b4504442-a4ee-5c85-aa45-22a37c8b73f1",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name",
    display_name="Torkoal",
    searchable_by=["Torkoal", "Basic", "Torkoal"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=324,
    abilities=[
        Attack(
            title="Fire Fling",
            game_text="Put 4 Fire Energy cards from your discard pile into your hand.",
            cost={PokemonTypes.FIRE: 1},
            effect=recover_from_discard(_is_fire_energy, count=4, minimum=0),
        ),
        Attack(
            title="Kindle",
            game_text="Discard an Energy from this Pok\u00e9mon. If you do, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)