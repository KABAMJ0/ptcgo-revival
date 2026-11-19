from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9550805-0fbf-5e88-9ade-3281ef3c4702",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name",
    display_name="Goomy",
    searchable_by=["Goomy", "Basic", "Goomy"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="ME4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=704,
    abilities=[
        Attack(
            title="Absorb",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=heal_attack(30),
        ),
    ],
)