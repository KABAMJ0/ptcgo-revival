from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="60337099-dd80-55eb-9009-e248b3b9df7c",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armarouge.Name",
    display_name="Armarouge",
    searchable_by=["Armarouge", "Stage 1", "Armarouge"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Ability(
            title="Fire Off",
            game_text="As often as you like during your turn, you may move a Fire Energy from 1 of your Benched Pok\u00e9mon to your Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Flame Cannon",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=unimplemented,
        ),
    ],
)