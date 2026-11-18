from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a77fd8f0-b733-5fd4-8bf3-efa9a79ff5ce",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="DP1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    family_id=355,
    abilities=[
        Ability(
            title="Dark Palm",
            game_text="Once during your turn (before your attack), if your opponent has 4 or more Benched Pok\u00e9mon, you may choose 1 of them and shuffle that Pok\u00e9mon and all cards attached to it into his or her deck. This power can't be used if Dusknoir if affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Hard Feelings",
            game_text="Put 5 damage counters on the Defending Pok\u00e9mon. Then, count the number of Prize cards your opponent has taken and put that many damage counters on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)