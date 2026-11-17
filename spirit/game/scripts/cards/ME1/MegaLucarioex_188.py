from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="71b51bd1-7b62-5576-bd19-f61500523e25",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaLucarioex.Name",
    display_name="Mega Lucario ex",
    searchable_by=["Mega Lucario ex", "Stage 1", "MEGA", "ex", "MegaLucarioex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=188,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Attack(
            title="Aura Jab",
            game_text="Attach up to 3 Basic Fighting Energy cards from your discard pile to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=130,
            effect=unimplemented,
        ),
        Attack(
            title="Mega Brave",
            game_text="During your next turn, this Pok\u00e9mon can't use Mega Brave.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=270,
            effect=unimplemented,
        ),
    ],
)