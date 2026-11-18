from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5d96b5ca-becd-5175-bd47-96f5e297608e",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garganacl.Name",
    display_name="Garganacl",
    searchable_by=["Garganacl", "Stage 2", "Garganacl"],
    subtypes=["Stage 2"],
    collector_number=202,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name",
    family_id=932,
    abilities=[
        Ability(
            title="Energizing Rock Salt",
            game_text="Once during your turn, you may attach a Basic Fighting Energy card from your discard pile to 1 of your Pok\u00e9mon. If you attached Energy to a Pok\u00e9mon in this way, heal 30 damage from that Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Land Crush",
            cost={PokemonTypes.FIGHTING: 3},
            damage=140,
        ),
    ],
)