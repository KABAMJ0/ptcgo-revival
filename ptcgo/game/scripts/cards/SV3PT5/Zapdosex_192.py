from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import has_energy_of
from ptcgo.game.session.passives import Passive, carrier_pokemon

class _VoltaicFloat(Passive):
    """No Retreat Cost while this Pokemon has any Lightning Energy attached."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        return 0 if has_energy_of("lightning")(pokemon) else cost

card = PokemonCardDef(
    guid="6044f90e-96ce-5f04-9ad6-06a5a71563a0",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdosex.Name",
    display_name="Zapdos ex",
    searchable_by=["Zapdos ex", "Basic", "ex", "Zapdosex"],
    subtypes=["Basic", "ex"],
    collector_number=192,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Ability(
            title="Voltaic Float",
            game_text="If this Pok\u00e9mon has any Lightning Energy attached, it has no Retreat Cost.",
            passive=_VoltaicFloat(),
        ),
        Attack(
            title="Multishot Lightning",
            game_text="This attack also does 90 damage to 1 of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)