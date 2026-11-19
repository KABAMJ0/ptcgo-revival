from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="5f9913f1-2b63-5627-a570-13329a022941",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bonsly.Name",
    display_name="Bonsly",
    searchable_by=["Bonsly", "Basic", "Bonsly"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    family_id=438,
    abilities=[
        Attack(
            title="Blubbering",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={},
            damage=10,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)