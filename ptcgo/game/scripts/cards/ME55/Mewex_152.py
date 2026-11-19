from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import switch_self_attack

card = PokemonCardDef(
    guid="fe6523cd-b0a8-5014-9d32-532683a1473d",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewex.Name",
    display_name="Mew ex",
    searchable_by=["Mew ex", "Basic", "ex", "Mewex"],
    subtypes=["Basic", "ex"],
    collector_number=152,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=151,
    abilities=[
        Ability(
            title="Memory Helix",
            game_text="This Pok\u00e9mon can use the attacks of any of your Benched Pok\u00e9mon. (You still need the necessary Energy to use each attack.)",
            effect=unimplemented,
        ),
        Attack(
            title="Teleportation Burst",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=switch_self_attack(optional=True),
        ),
    ],
)