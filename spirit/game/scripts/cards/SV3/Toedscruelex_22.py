from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="074ee3b5-8d13-501c-a379-0fde07c1c1b1",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscruelex.Name",
    display_name="Toedscruel ex",
    searchable_by=["Toedscruel ex", "Stage 1", "ex", "Toedscruelex"],
    subtypes=["Stage 1", "ex"],
    collector_number=22,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name",
    family_id=948,
    abilities=[
        Ability(
            title="Protective Mycelium",
            game_text="Prevent all effects of attacks used by your opponent's Pok\u00e9mon done to all of your Pok\u00e9mon that have Energy attached. (Existing effects are not removed. Damage is not an effect.)",
            effect=unimplemented,
        ),
        Attack(
            title="Colony Rush",
            game_text="This attack does 40 more damage for each of your Benched Pok\u00e9mon that has any Grass Energy attached.",
            cost={PokemonTypes.GRASS: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)