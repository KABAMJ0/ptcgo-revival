from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="b63ff14d-7d72-5bc4-8670-21021ab84e3f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klawf.Name",
    display_name="Klawf",
    searchable_by=["Klawf", "Basic", "Klawf"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=950,
    abilities=[
        Attack(
            title="Vise Grip",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
        ),
        Attack(
            title="Adrenaline Hammer",
            game_text="This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=130,
            effect=condition_attack(self_conditions=(SpecialConditions.CONFUSED,)),
        ),
    ],
)