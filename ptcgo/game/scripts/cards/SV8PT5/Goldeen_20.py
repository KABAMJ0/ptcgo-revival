from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_discard_opponent_energy

card = PokemonCardDef(
    guid="d6ccf1e3-7462-5d62-b77d-e2717126c6e9",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goldeen.Name",
    display_name="Goldeen",
    searchable_by=["Goldeen", "Basic", "Goldeen"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=118,
    abilities=[
        Ability(
            title="Festival Lead",
            game_text="If Festival Grounds is in play, this Pok\u00e9mon may use an attack it has twice. If the first attack Knocks Out your opponent's Active Pok\u00e9mon, you may attack again after your opponent chooses a new Active Pok\u00e9mon.",
            effect=flip_gate(discard_opponent_energy_attack(1)),
        ),
        Attack(
            title="Whirlpool",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=flip_discard_opponent_energy(),
        ),
    ],
)