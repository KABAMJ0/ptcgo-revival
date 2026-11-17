from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="17093d99-d181-59bb-b059-1b23fe9cd71d",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    display_name="Shinx",
    searchable_by=["Shinx", "Basic", "Shinx"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=403,
    abilities=[
        Ability(
            title="Big Roar",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may switch out your opponent's Active Pok\u00e9mon to the Bench.\u00a0(Your opponent chooses the new Active Pok\u00e9mon.)",
            effect=unimplemented,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)