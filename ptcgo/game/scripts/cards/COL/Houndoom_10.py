from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a821f2ac-8dda-5ba7-a238-28e82050e7ea",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1", "Houndoom"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="COL",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Fire Counterattack",
            game_text="If your opponent has any Fighting Pok\u00e9mon in play, this attack does 20 damage plus 60 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Dark Roar",
            game_text="Your opponent discards a card from his or her hand.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)