from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bc602d2a-41de-50e0-b90f-c7769f1dd603",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=70,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    family_id=355,
    abilities=[
        Ability(
            title="Cursed Blast",
            game_text="Once during your turn, you may put 13 damage counters on 1 of your opponent's Pok\u00e9mon. If you use this Ability, this Pok\u00e9mon is Knocked Out.",
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Bind",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)