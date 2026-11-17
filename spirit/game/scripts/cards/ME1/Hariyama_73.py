from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1bcab814-7a45-5421-b692-de7f17cb5e6c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name",
    display_name="Hariyama",
    searchable_by=["Hariyama", "Stage 1", "Hariyama"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    family_id=296,
    abilities=[
        Ability(
            title="Heave-Ho Catcher",
            game_text="Once during your turn, when you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may use this Ability. Switch in 1 of your opponent's Benched Pok\u00e9mon to the Active Spot.",
            effect=unimplemented,
        ),
        Attack(
            title="Wild Press",
            game_text="This Pok\u00e9mon also does 70 damage to itself.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=210,
            effect=unimplemented,
        ),
    ],
)