from ptcgo.game.card_effects.attacks_common import mill_scaled_damage
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_energy_card
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


def _fighting_energy(card) -> bool:
    return energy_provides_type(card, PokemonTypes.FIGHTING.value)

card = PokemonCardDef(
    guid="9ed5586f-91b4-54c9-8090-85479d367a85",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RhyperiorLVX.Name",
    display_name="Rhyperior LV.X",
    searchable_by=["Rhyperior LV.X", "Level-Up", "RhyperiorLVX"],
    subtypes=["Level-Up"],
    collector_number=145,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name",
    family_id=464,
    abilities=[
        Attack(
            title="Hard Crush",
            game_text="Discard the top 5 cards from your deck. This attack does 50 damage for each Energy card you discarded.",
            cost={},
            damage=50,
            damage_operator="x",
            effect=mill_scaled_damage(5, 50, pred=is_energy_card),
        ),
        Attack(
            title="Upthrow",
            game_text="Search your discard pile for all Fighting Energy cards, show them to your opponent, and shuffle them into your deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=recover_from_discard(_fighting_energy, count=99, minimum=0,
                                        to="deck_shuffle"),
        ),
    ],
)