from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import reduce_defender_attacks

card = PokemonCardDef(
    guid="70aa25bb-513e-5056-86ee-bc27fc37a6e2",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name",
    display_name="Pawmi",
    searchable_by=["Pawmi", "Basic", "Pawmi"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="ME2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=921,
    abilities=[
        Attack(
            title="Growl",
            game_text="During your opponent's next turn, attacks used by the Defending Pok\u00e9mon do 30 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=reduce_defender_attacks(30),
        ),
        Attack(
            title="Tiny Charge",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)