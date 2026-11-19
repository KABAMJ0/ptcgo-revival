from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import aqua_return


card = PokemonCardDef(
    guid="98afde13-1e50-55ea-b5ed-df3b68b64ae6",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lokix.Name",
    display_name="Lokix",
    searchable_by=["Lokix", "Stage 1", "Lokix"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name",
    family_id=919,
    abilities=[
        Attack(
            title="Low Kick",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Jumping Shot",
            game_text="Shuffle this Pok\u00e9mon and all attached cards into your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=aqua_return,
        ),
    ],
)