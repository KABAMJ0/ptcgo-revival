from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ba416732-8dd7-54af-8580-e8c5efa88055",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name",
    display_name="Masquerain",
    searchable_by=["Masquerain", "Stage 1", "Masquerain"],
    subtypes=["Stage 1"],
    collector_number=104,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    family_id=283,
    abilities=[
        Attack(
            title="Frightening Pattern",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't use attacks.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Bug Out",
            game_text="Reveal the bottom 7 cards of your deck, and this attack does 50 damage for each Pok\u00e9mon you find there that has the Bug Out attack. Then, shuffle any revealed Pok\u00e9mon back into your deck. Discard the other cards.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)