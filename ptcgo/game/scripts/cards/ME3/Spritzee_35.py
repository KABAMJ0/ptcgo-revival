from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="64abd100-16d5-5bcf-a94e-3b5d5a225706",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name",
    display_name="Spritzee",
    searchable_by=["Spritzee", "Basic", "Spritzee"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="ME3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=682,
    abilities=[
        Attack(
            title="Sweet Scent",
            game_text="Heal 30 damage from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_attack(30),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)