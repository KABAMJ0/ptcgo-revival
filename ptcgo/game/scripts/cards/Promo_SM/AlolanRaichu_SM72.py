from ptcgo.game.card_effects.attacks_common import damage_per, count_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon

class SurgeSurferPassive(Passive):
    """No Retreat Cost while any Stadium card is in play."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier_pokemon(carrier):
            return cost
        slot = board.find_global_area("activeStadium") if board is not None else None
        return 0 if (slot is not None and slot.children) else cost


card = PokemonCardDef(
    guid="c6dcaf69-e5b6-5ff1-bb9b-d804cc1bd25d",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRaichu.Name",
    display_name="Alolan Raichu",
    searchable_by=["Alolan Raichu", "Stage 1", "AlolanRaichu"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Ability(
            title="Surge Surfer",
            game_text="If there is any Stadium card in play, this Pok\u00e9mon has no Retreat Cost.",
            passive=SurgeSurferPassive(),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 20 more damage times the amount of Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 20, base=70),
        ),
    ],
)