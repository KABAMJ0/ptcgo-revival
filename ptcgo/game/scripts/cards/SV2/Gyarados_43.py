from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eccff449-188c-535a-9dec-79d8f4cad314",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Revengeful Storm",
            game_text="If you have more Prize cards remaining than your opponent, this attack does 100 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Berserker Tackle",
            game_text="This Pok\u00e9mon also does 50 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=recoil_attack(50),
        ),
    ],
)