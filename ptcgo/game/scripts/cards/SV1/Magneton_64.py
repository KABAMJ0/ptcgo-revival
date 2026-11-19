from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="890823c5-3526-5e9b-94f1-2e30318758c7",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1", "Magneton"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Lightning Ball",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
        Attack(
            title="Explosion",
            game_text="This Pok\u00e9mon also does 90 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=90,
            effect=recoil_attack(90),
        ),
    ],
)