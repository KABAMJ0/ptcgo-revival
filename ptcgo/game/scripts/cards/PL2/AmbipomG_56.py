from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="b8b07fed-732a-519b-9cfd-828d86b4a50d",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AmbipomG.Name",
    display_name="Ambipom G",
    searchable_by=["Ambipom G", "Basic", "SP", "AmbipomG"],
    subtypes=["Basic", "SP"],
    collector_number=56,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=424,
    abilities=[
        Attack(
            title="Tail Code",
            game_text="Move an Energy card attached to the Defending Pok\u00e9mon to another of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Snap Attack",
            game_text="If the Defending Pok\u00e9mon has any Energy cards attached to it, this attack's base damage is 20 instead of 60.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)