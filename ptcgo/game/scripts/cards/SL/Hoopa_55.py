from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6d8f7be4-8059-5bae-a73c-ff22f17bad24",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoopa.Name",
    display_name="Hoopa",
    searchable_by=["Hoopa", "Basic", "Hoopa"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="SL",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=720,
    abilities=[
        Ability(
            title="Scoundrel Guard",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon by your opponent's Pok\u00e9mon-GX or Pok\u00e9mon-EX.",
            effect=unimplemented,
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)