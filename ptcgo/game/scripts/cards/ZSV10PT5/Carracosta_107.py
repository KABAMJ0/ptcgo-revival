from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="840a96c7-a36d-557e-a9e1-d5fd9a8aca7a",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carracosta.Name",
    display_name="Carracosta",
    searchable_by=["Carracosta", "Stage 2", "Carracosta"],
    subtypes=["Stage 2"],
    collector_number=107,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tirtouga.Name",
    family_id=564,
    abilities=[
        Ability(
            title="Mighty Shell",
            game_text="Prevent all damage from and effects of attacks done to this Pok\u00e9mon by your opponent's Pok\u00e9mon that have any Special Energy attached.",
            effect=unimplemented,
        ),
        Attack(
            title="Big Bite",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=unimplemented,
        ),
    ],
)