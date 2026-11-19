from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import Passive, is_in_active_spot
from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.models.board import EnergyEntity


class _EmergencyExit(Passive):
    """Emergency Exit: no Retreat Cost while this Pokemon holds 2 Energy or less."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier)
        if pokemon is not holder:
            return cost
        attached = [c for c in getattr(holder, "children", []) or []
                    if isinstance(c, EnergyEntity)]
        return 0 if len(attached) <= 2 else cost

card = PokemonCardDef(
    guid="bdc28478-cc70-5ac2-9dca-0dc2b9e2de0f",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golisopod.Name",
    display_name="Golisopod",
    searchable_by=["Golisopod", "Stage 1", "Golisopod"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="SM11",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    family_id=767,
    abilities=[
        Ability(
            title="Emergency Exit",
            game_text="If this Pok\u00e9mon has 2 or fewer Energy attached to it, it has no Retreat Cost.",
            passive=_EmergencyExit(),
        ),
        Attack(
            title="First Impression",
            game_text="If this Pok\u00e9mon was on the Bench and became your Active Pok\u00e9mon this turn, this attack does 60 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)