from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="57b2734a-f836-5dd2-aaf9-9032398eac0e",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noivern.Name",
    display_name="Noivern",
    searchable_by=["Noivern", "Stage 1", "Noivern"],
    subtypes=["Stage 1"],
    collector_number=157,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    family_id=714,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Enhanced Blade",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool attached, this attack does 70 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            damage=70,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)