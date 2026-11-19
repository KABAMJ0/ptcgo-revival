from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="658be6b1-7434-54a7-9f5c-96883adf08bd",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HolonsVoltorb.Name",
    display_name="Holon's Voltorb",
    searchable_by=["Holon's Voltorb", "Basic", "HolonsVoltorb"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="EX11",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=100,
    abilities=[
        Attack(
            title="Thundershock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)