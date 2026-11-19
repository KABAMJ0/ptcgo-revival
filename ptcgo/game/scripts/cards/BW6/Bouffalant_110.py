from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.attacks_common import flip_discard_opponent_energy
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
card = PokemonCardDef(
    guid="5b93cdfa-e7a7-51ba-95f9-78eaba1ad62d",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name",
    display_name="Bouffalant",
    searchable_by=["Bouffalant", "Basic", "Bouffalant"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=626,
    abilities=[
        Ability(
            title="Bouffer",
            game_text="Any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            effect=flip_gate(discard_opponent_energy_attack(1)),
        ),
        Attack(
            title="Gold Breaker",
            game_text="If the Defending Pok\u00e9mon is a Pok\u00e9mon-EX, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)