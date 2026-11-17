from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fbea03e7-630c-5178-a296-821dba756813",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaCameruptex.Name",
    display_name="Mega Camerupt ex",
    searchable_by=["Mega Camerupt ex", "Stage 1", "MEGA", "ex", "MegaCameruptex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=22,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    family_id=322,
    abilities=[
        Attack(
            title="Roasting Heat",
            game_text="If your opponent's Active Pok\u00e9mon is Burned, this attack does 160 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Volcanic Meteor",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=280,
            effect=unimplemented,
        ),
    ],
)