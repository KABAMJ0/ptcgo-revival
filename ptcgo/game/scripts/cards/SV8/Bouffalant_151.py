from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack, lock_self_attack
card = PokemonCardDef(
    guid="d764d529-7ab5-5157-8455-75a3fca40490",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name",
    display_name="Bouffalant",
    searchable_by=["Bouffalant", "Basic", "Bouffalant"],
    subtypes=["Basic"],
    collector_number=151,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=626,
    abilities=[
        Attack(
            title="Ready to Ram",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if this Pok\u00e9mon is Knocked Out), put 6 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=lock_self_attack(),
        ),
        Attack(
            title="Smashing Headbutt",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=150,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)