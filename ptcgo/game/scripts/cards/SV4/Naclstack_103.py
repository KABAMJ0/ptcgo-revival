from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="26930fc6-e2a1-5f59-84c6-57c153209ebd",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name",
    display_name="Naclstack",
    searchable_by=["Naclstack", "Stage 1", "Naclstack"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name",
    family_id=932,
    abilities=[
        Attack(
            title="Rocky Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
            effect=recoil_attack(30),
        ),
    ],
)